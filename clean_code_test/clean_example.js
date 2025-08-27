/**
 * Clean JavaScript code that should pass linting checks
 */

/**
 * Calculate the sum of an array of numbers
 * @param {number[]} numbers - Array of numbers to sum
 * @returns {number} The sum of all numbers
 */
function calculateSum(numbers) {
  if (!Array.isArray(numbers)) {
    throw new TypeError('Input must be an array');
  }

  return numbers.reduce((acc, num) => {
    if (typeof num !== 'number') {
      throw new TypeError('All elements must be numbers');
    }
    return acc + num;
  }, 0);
}

/**
 * Class representing a data processor
 */
class DataProcessor {
  /**
   * Create a data processor
   * @param {string} name - The processor name
   * @param {Object} options - Configuration options
   */
  constructor(name, options = {}) {
    this.name = name;
    this.options = {
      batchSize: 100,
      timeout: 5000,
      ...options
    };
    this.processedCount = 0;
  }

  /**
   * Process a batch of data
   * @param {Array} data - Data to process
   * @returns {Promise<Array>} Processed data
   */
  async processBatch(data) {
    const results = [];
    
    for (const item of data) {
      const processed = await this.processItem(item);
      results.push(processed);
      this.processedCount++;
    }
    
    console.log(`Processed ${data.length} items`);
    return results;
  }

  /**
   * Process a single item
   * @param {Object} item - Item to process
   * @returns {Promise<Object>} Processed item
   */
  async processItem(item) {
    // Simulate async processing
    await new Promise(resolve => setTimeout(resolve, 10));
    
    return {
      id: item.id,
      processed: true,
      timestamp: new Date().toISOString(),
      processor: this.name,
      data: item
    };
  }

  /**
   * Get processing statistics
   * @returns {Object} Statistics object
   */
  getStatistics() {
    return {
      processorName: this.name,
      batchSize: this.options.batchSize,
      totalProcessed: this.processedCount
    };
  }
}

/**
 * Filter array by predicate function
 * @param {Array} array - Array to filter
 * @param {Function} predicate - Filter function
 * @returns {Array} Filtered array
 */
const filterArray = (array, predicate) => {
  if (!Array.isArray(array)) {
    return [];
  }
  
  if (typeof predicate !== 'function') {
    throw new TypeError('Predicate must be a function');
  }
  
  return array.filter(predicate);
};

/**
 * Utility functions for string manipulation
 */
const StringUtils = {
  /**
   * Capitalize first letter of string
   * @param {string} str - Input string
   * @returns {string} Capitalized string
   */
  capitalize(str) {
    if (typeof str !== 'string') {
      return '';
    }
    return str.charAt(0).toUpperCase() + str.slice(1);
  },

  /**
   * Check if string is empty or whitespace
   * @param {string} str - String to check
   * @returns {boolean} True if empty or whitespace
   */
  isBlank(str) {
    return !str || !str.trim();
  },

  /**
   * Truncate string to specified length
   * @param {string} str - String to truncate
   * @param {number} maxLength - Maximum length
   * @param {string} suffix - Suffix to append
   * @returns {string} Truncated string
   */
  truncate(str, maxLength, suffix = '...') {
    if (typeof str !== 'string') {
      return '';
    }
    
    if (str.length <= maxLength) {
      return str;
    }
    
    return str.slice(0, maxLength - suffix.length) + suffix;
  }
};

// Example usage
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    calculateSum,
    DataProcessor,
    filterArray,
    StringUtils
  };
}